import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Leaf here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Leaf extends Actor
{
    /**
     * Act - do whatever the Leaf wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    {
        move(8);
        int angle = Greenfoot.getRandomNumber(90);
        turn(angle);
    }    
}
