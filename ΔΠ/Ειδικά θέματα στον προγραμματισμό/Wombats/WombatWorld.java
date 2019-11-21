import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Ένα παιχνίδι με τον Φασκωλόμυς που χάφτει φύλλα.
 * 
 * @author Ευστάθιος Ιωσηφίδης, Ελένη Κάλφα 
 * @version 0.1
 */
public class WombatWorld extends World
{

    /**
     * Constructor for objects of class WombatWorld.
     * 
     */
    public WombatWorld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(600, 400, 1);
        Wombat arkoudaki = new Wombat();
        addObject(arkoudaki,100,100);
        Leaf fillo=new Leaf();
        addObject(fillo,200,200);
        Leaf fillo1=new Leaf();
        addObject(fillo1,443,160);
        Leaf fillo2=new Leaf();
        addObject(fillo2,398,335);
    }
}
