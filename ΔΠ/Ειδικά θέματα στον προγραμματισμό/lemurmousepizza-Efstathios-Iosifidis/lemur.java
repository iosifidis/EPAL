import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class lemur here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class lemur extends Actor
{
    /**
     * Act - do whatever the lemur wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    {
        randomMove();
        touchingMouse();// Add your action code here.
    } 
    
    void touchingMouse()
    {
        if (isTouching(mouse.class))
        {
            removeTouching(mouse.class);
            System.out.println ("Sorry - GAME OVER");
            Greenfoot.stop();
        }
    }
    void randomMove() 
    {
        move(1);
        if (Greenfoot.getRandomNumber(100)>60)
        {
            turn(90);
        }
    }
}
