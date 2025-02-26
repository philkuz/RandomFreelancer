package com.philkuz.javadrive;



import java.nio.file.*;
import java.io.IOException;

 
/**
 * Example to watch a directory (or tree) for changes to files.
 */
 
public class JavaDrive {
	public static String googleDrivePath = "C:\\Users\\pkusnetsov\\Google Drive";
	public static String logDirectory = "logs\\";
	public static int windowLength = 700;
	public static int windowHeight = 300;
  
    public static void main(String[] args) throws IOException {
    	//here is where you set the Path
    	WindowHandler window = new WindowHandler();
    	Path dir = Paths.get(googleDrivePath);
    	DirWatch watcher = new DirWatch(dir, window);
    	watcher.processEvents();
    }
}