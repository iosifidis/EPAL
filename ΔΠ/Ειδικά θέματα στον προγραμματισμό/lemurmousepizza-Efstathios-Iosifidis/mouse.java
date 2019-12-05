import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class mouse here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class mouse extends Actor
{
    private Counter counter;
    /**
     * Act - do whatever the mouse wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    int score = 0;
    public void act() 
    {
        checkKeyboard();
        touchingCheese();
    }  
    
    void checkKeyboard()
    {
        
        if (Greenfoot.isKeyDown("left"))
        {
            turn(-90);
        }
        if (Greenfoot.isKeyDown("right"))
        {
            turn(90);
            
        }
        if (Greenfoot.isKeyDown("up")){
            
            move(1);
        }
        if (Greenfoot.isKeyDown("down")){
            
            turn(90);
        }
    }
    void touchingCheese()
    {
        if (isTouching(cheese.class))
        {
            
            counter.add(1);
            removeTouching(cheese.class);
            score = score + 1;
            if (score == 5)
            {
               System.out.println ("Congratulations - Your Score = 5 - Enter Next Level");
               Greenfoot.stop();
            }
        }
    }
    public mouse (Counter pointcounter)
    {
        counter=pointcounter;
    }
}
