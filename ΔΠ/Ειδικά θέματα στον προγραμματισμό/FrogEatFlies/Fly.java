import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Fly here.
 * 
 * @author Ευστάθιος Ιωσηφίδης 
 * @version 1.0
 */
public class Fly extends Animal
{
    /**
     * Act - do whatever the Fly wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    {
        move(8);
        if (isAtEdge())
            {
                turn(15);
            }
    }    
}
