import com.google.api.client.auth.oauth2.Credential;
import com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp;
import com.google.api.client.extensions.jetty.auth.oauth2.LocalServerReceiver;
import com.google.api.client.googleapis.auth.oauth2.GoogleAuthorizationCodeFlow;
import com.google.api.client.googleapis.auth.oauth2.GoogleClientSecrets;
import com.google.api.client.googleapis.javanet.GoogleNetHttpTransport;
import com.google.api.client.http.HttpTransport;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.util.store.FileDataStoreFactory;

import com.google.api.services.drive.DriveScopes;
import com.google.api.services.drive.model.*;
import com.google.api.services.drive.Drive;
import com.google.api.services.drive.Drive.Changes;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.UUID;

public class JavaDrive {
    /** Amount of time between refreshes in ms **/
    private static final int REFRESH_TIME = 60000;
    /** Application name. */
    private static final String APPLICATION_NAME =
        "Java Drive";

    /** Directory to store user credentials for this application. */
    private static final java.io.File DATA_STORE_DIR = new java.io.File(
        System.getProperty("user.home"), ".credentials/java-drive");

    /** Global instance of the {@link FileDataStoreFactory}. */
    private static FileDataStoreFactory DATA_STORE_FACTORY;

    /** Global instance of the JSON factory. */
    private static final JsonFactory JSON_FACTORY =
        JacksonFactory.getDefaultInstance();

    /** Global instance of the HTTP transport. */
    private static HttpTransport HTTP_TRANSPORT;

    /** Global instance of the scopes required by this quickstart. */
    private static final List<String> SCOPES =
        new ArrayList<String>(DriveScopes.all());
    static {
        try {
            HTTP_TRANSPORT = GoogleNetHttpTransport.newTrustedTransport();
            DATA_STORE_FACTORY = new FileDataStoreFactory(DATA_STORE_DIR);
        } catch (Throwable t) {
            t.printStackTrace();
            System.exit(1);
        }
    }
    /** Flag which signals whether the program should use lastChangeId if startChangeId is null**/
    private static boolean useLastId = true;
    /** The lastChangeId seen by the program. Adding one will ignore all changes up to this point**/
    private static Long lastChangeId = null;

    /**
     * Creates an authorized Credential object.
     * @return an authorized Credential object.
     * @throws IOException
     */
    public static Credential authorize() throws IOException {
        // Load client secrets.
        InputStream in =
            JavaDrive.class.getResourceAsStream("/client_secret.json");
        GoogleClientSecrets clientSecrets =
            GoogleClientSecrets.load(JSON_FACTORY, new InputStreamReader(in));

        // Build flow and trigger user authorization request.
        GoogleAuthorizationCodeFlow flow =
                new GoogleAuthorizationCodeFlow.Builder(
                        HTTP_TRANSPORT, JSON_FACTORY, clientSecrets, SCOPES)
                .setDataStoreFactory(DATA_STORE_FACTORY)
                .setAccessType("offline")
                .build();
        Credential credential = new AuthorizationCodeInstalledApp(
            flow, new LocalServerReceiver()).authorize("user");
        System.out.println(
                "Credentials saved to " + DATA_STORE_DIR.getAbsolutePath());
        return credential;
    }

    /**
     * Build and return an authorized Drive client service.
     * @return an authorized Drive client service
     * @throws IOException
     */
    public static Drive getDriveService() throws IOException {
        Credential credential = authorize();
        return new Drive.Builder(
                HTTP_TRANSPORT, JSON_FACTORY, credential)
                .setApplicationName(APPLICATION_NAME)
                .build();
    }
   
    private static List<Change> retrieveChanges(Drive service, Long startChangeId) throws IOException {
        List<Change> result = new ArrayList<Change>();
        Changes.List request = service.changes().list();
        if(startChangeId != null)
        {
            request.setStartChangeId(startChangeId);
        }
        else if(useLastId && lastChangeId != null)
        {
            request.setStartChangeId(lastChangeId+1);
        }
        do {
            try {
                ChangeList changes = request.execute();

                result.addAll(changes.getItems());
                request.setPageToken(changes.getNextPageToken());
            } catch (IOException e) {
                System.out.println("An error occurred: " + e);
                request.setPageToken(null);
            }
        } while (request.getPageToken() != null &&
            request.getPageToken().length() > 0);
        if(result.size() > 0 )
            lastChangeId = result.get(result.size()-1).getId();
        return result;
    }
    /*
    private static List<String> getChangedFiles(Drive service, Long startChangeId) throws IOException{
        List<String> fileIds = new ArrayList<String>();
        List<Change> changes = retrieveChanges(service, startChangeId);
        for(Change change : changes){
          //change.getFile().getOriginalFilename(),
            fileIds.add(change.getFileId());
        }
        return fileIds;
    }
    /*
    * Gets the changedfiles from the last saved lastChangeId (which is adjusted from the last call)
    * @return a list of fileIds that have been changed since the last change check (marked by lastChangeId)
    */ 
    /*
    private static List<String> getChangedFiles(Drive service) throws IOException
    {        
        List<String> fileIds = new ArrayList<String>();
        List<Change> changes = retrieveChanges(service, null);
        for(Change change : changes){
          //change.getFile().getOriginalFilename(),
            fileIds.add(change.getFileId());
        }
        
        return fileIds;
    }*/
    private static List<File> getChangeFiles(Drive service, Long startChangeId) throws IOException
    {
      List<File> files = new ArrayList<File>();
      List<Change> changes = retrieveChanges(service, startChangeId);
      for(Change change: changes) {
          files.add(getFile(service, change.getFileId()));
      }
      return files;
    }
    private static void printChangedFiles(Drive service) throws IOException{
      List<Change> changes = retrieveChanges(service, null);
      for(Change change: changes){
        String deleted = change.getDeleted() ? "Deleted" : "Changed";
        System.out.printf("%s: %s; %s\r\n", change.getModificationDate(), change.getFileId(), deleted);
      }
    }
     /**
   * Print a file's metadata.
   *
   * @param service Drive API service instance.
   * @param fileId ID of the file to print metadata for.
   */
  private static File getFile(Drive service, String fileId) throws IOException {
      return service.files().get(fileId).execute();
  }
  private static void printFile(Drive service, String fileId) {

    try {
      File file = service.files().get(fileId).execute();

      System.out.println("Title: " + file.getTitle());
      System.out.println("Description: " + file.getDescription());
      System.out.println("MIME type: " + file.getMimeType());
    } catch (IOException e) {
      System.out.println("An error occured with " + fileId);
    }
  }
    public static void monitor() throws IOException {
      Drive service = getDriveService();
      
      for(;;)
      {
        doStuffMethod(retrieveChanges(service, null));
        
        System.out.println("Sleeping thread");
        try{
        Thread.sleep(REFRESH_TIME);
      }catch(InterruptedException e){}

      }

    }
    public static void doStuffMethod(List<Change> changes) throws IOException {
      for(Change change : changes)
      {
        String fileId = change.getFileId();
        System.out.printf("ID: %s\r\n",  fileId);
      }
    }
    public static void main(String[] args) throws IOException {
        // Build a new authorized API client service.
        monitor();
        // Drive service = getDriveService();
        // printChangedFiles(service);        
        
        // List<String> fileIds = getChangedFiles(service, new Long(10300));

        // for(String fileId: fileIds){
        //   //change.getFile().getOriginalFilename(),
        //     System.out.printf("ID: %s\r\n",  fileId);
        //     printFile(service, fileId);
        // }
        // System.out.printf("There should be no changes after this point\n");

        // fileIds = getChangedFiles(service);

        
    }

}