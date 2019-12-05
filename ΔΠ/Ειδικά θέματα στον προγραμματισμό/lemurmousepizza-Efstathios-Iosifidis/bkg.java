import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Ο βασιλιάς Τζούλιαν και ο Ρατατούης
 * 
 * @author Ευστάθιος Ιωσηφίδης 
 * @version 0.1
 */
public class bkg extends World
{

    /**
     * Constructor for objects of class bkg.
     * 
     */
    public bkg()
    {    
        // Create a new world with 8x8 cells with a cell size of 60x60 pixels.
        super(8, 8, 60); 
        addObject();
        prepare();
    }
    
    void addObject()
    {
        addObject(new cheese(), 2, 3);
        addObject(new lemur(), 8, 8);
        addObject(new cheese(), Greenfoot.getRandomNumber(9), Greenfoot.getRandomNumber(9));
    }
     
    /**
     * Prepare the world for the start of the program.
     * That is: create the initial objects and add them to the world.
     */
    private void prepare()
    {
        Counter counter = new Counter();
        addObject(counter,69,40);
        mouse mouse = new mouse(counter);
        addObject(mouse,1,2);
        cheese cheese = new cheese();
        addObject(cheese,3,2);
        cheese cheese2 = new cheese();
        addObject(cheese2,1,5);
        cheese cheese3 = new cheese();
        addObject(cheese3,6,5);
        counter.setLocation(1,0);
    }
}
