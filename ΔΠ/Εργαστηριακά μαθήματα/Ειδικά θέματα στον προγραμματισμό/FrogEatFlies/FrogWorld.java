import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class FrogWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class FrogWorld extends World
{

    /**
     * Constructor for objects of class FrogWorld.
     * 
     */
    public FrogWorld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(600, 400, 1); 
        Frog kermit = new Frog();
        addObject(kermit, 100, 100);
        
        Fly myga = new Fly();
        addObject( myga, 200, 200);
        
        Fly myga1 = new Fly();
        addObject( myga1, 443, 160);
        
        Fly myga2 = new Fly();
        addObject( myga2, 398, 335);
    }

    /**
     * Prepare the world for the start of the program.
     * That is: create the initial objects and add them to the world.
     */
    private void prepare()
    {
        Frog frog = new Frog();
        addObject(frog,55,227);
        Fly fly = new Fly();
        addObject(fly,311,70);
        Fly fly2 = new Fly();
        addObject(fly2,521,224);
        Fly fly3 = new Fly();
        addObject(fly3,258,345);
    }
}
