class Game(object):
  	static int animationcounter = 0;
	static int framewidth = 512 + 240;
	static int frameheight = 480;
	static Character background = new Character(0, 0, 512, 4192, "background.png", "blank");
	static Character tora = new Character(100, 30, 32, 32, "tora1.png", "character");
	static Character weapon = new Character(0, 0, 10, 10, "", "weapon");
	static Character ui = new Character(512, 0, 240, 480, "red.png", "blank");
	static LinkedList<Character> collectedTreasure = new LinkedList<Character>();
	static Character bigChest = new Character(600, 200, 64, 64, "", "blank");
	String maptype;
	static int collectedTreasures = 0;
	static String gameStatus = "playing";
	static LinkedList<Obstacle> obstacles = new LinkedList<Obstacle>();
	static LinkedList<Item> treasures = new LinkedList<Item>();

	static LinkedList<Clip> sounds = new LinkedList<Clip>();
	static Clip bgm;

	int camx = 0;
	int camy = 0;
	static camera Camera = new camera(0, 0);

    public Game() {
		addKeyListener(new KeyListener() {
			@Override
			public void keyTyped(KeyEvent e) {
			}

			@Override
			public void keyReleased(KeyEvent e) {
				tora.keyReleased(e);
			}

			@Override
			public void keyPressed(KeyEvent e) {
				tora.keyPressed(e);
			}
		});
		setFocusable(true);
	}
    def move():
        background.move()
        tora.move()
        for i in obstacles:
            obstacles.get(i).move()
    move()
    
    def update():
        background.update()
        if Camera.movement != "stop":
            for i in obstacles: 
                obstacles.get(i).update()
            
        for i in treasures:
            treasures.get(i).update();
            tora.update();
    update()
    
    def paintComponent():
        g.translate(0, 0)
        g.translate(-Camera.x, -Camera.y)
        background.paint(g2d)
        for i in obstacles:
            obstacles.get(i).paint(g2d)
        for i in treasures:
            treasures.get(i).paint(g2d)
            g.translate(Camera.x, Camera.y)
            tora.paint(g2d)
            ui.paint(g2d)
        for i in collectedTreasure:
            collectedTreasure.get(i).paint(g2d)
            bigChest.paint(g2d)
            g.setColor(Color.blue)
            g.fillRect(600, 50, tora.health*10,10)
            g.setColor(Color.black)
            g.fillRect(600+tora.health*10,50,(10-tora.health)*10,10)
    paintComponent()
    
    def main(): 
        finalwidth = framewidth
        finalheight = frameheight
        Game game = new Game()
        game.maptype = "default"
        # frame.setSize(finalwidth, finalheight)
        game.setPreferredSize(new Dimension(finalwidth, finalheight)
        Map.createMap()
        print(frame.getContentPane().getSize())
        Thread.sleep(1000)
    main()
    
    def draw():
        while gameStatus == "playing":
        game.move()
        tora.up = true
        tora.down = true
        tora.left = true
        tora.right = true
        game.update()
        Camera.update()
        game.repaint()
        Thread.sleep(25)
    draw()
