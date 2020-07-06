import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Ο βάτραχος (Frog) είναι ένα αντικείμενο που κινείται μέσα στον Κόσμο κι όταν βρει μύγες τις τρώει..
 * 
 * @author Ευστάθιος Ιωσηφίδης 
 * @version 1.0
 */
public class Frog extends Animal
{
    /**
     * Act - do whatever the Frog wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    {
        move(4);
        if (isAtEdge())
            {
                turn(5);
            }
     }    
}
