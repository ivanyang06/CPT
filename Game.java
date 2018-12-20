package game;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

import java.util.LinkedList;
import java.util.Scanner;

import java.io.File;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineEvent;

@SuppressWarnings("serial")
public class Game extends JPanel {
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

	private void move() {
		background.move();
		tora.move();
		for (int i = 0; i < obstacles.size(); i++) {
			obstacles.get(i).move();
		}
	}

	private void update() {
		background.update();
		if (Camera.movement != "stop") {
			for (int i = 0; i < obstacles.size(); i++) {
				obstacles.get(i).update();
			}
		}
		for (int i = 0; i < treasures.size(); i++) {
			treasures.get(i).update();
		}
		tora.update();
	}

	public static void playSound(String src, String type) {
		if (type == "bgm") {
			String soundName = src;
			try {
				AudioInputStream audioInputStream = AudioSystem
						.getAudioInputStream(new File(soundName).getAbsoluteFile());
				bgm = AudioSystem.getClip();
				bgm.open(audioInputStream);
				bgm.start();
			} catch (Exception ex) {
				ex.printStackTrace();
				System.out.println("Exception: " + ex.getMessage());
			}
		} else {
			String soundName = src;
			try {
				AudioInputStream audioInputStream = AudioSystem
						.getAudioInputStream(new File(soundName).getAbsoluteFile());
				Clip tempsound = AudioSystem.getClip();
				sounds.add(tempsound);
				sounds.get(sounds.size() - 1).addLineListener(e -> {
					if (e.getType() == LineEvent.Type.STOP) {
						sounds.remove(sounds.size()-1);
					}
				});
				sounds.get(sounds.size() - 1).open(audioInputStream);
				sounds.get(sounds.size() - 1).start();
			} catch (Exception ex) {
				ex.printStackTrace();
				System.out.println("Exception: " + ex.getMessage());
			}
		}
	}

	@Override
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		Graphics2D g2d = (Graphics2D) g;
		g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_OFF);
		g.translate(0, 0);
		g.translate(-Camera.x, -Camera.y);
		background.paint(g2d);
		for (int i = 0; i < obstacles.size(); i++) {
			obstacles.get(i).paint(g2d);
		}
		for (int i = 0; i < treasures.size(); i++) {
			treasures.get(i).paint(g2d);
		}
		g.translate(Camera.x, Camera.y);
		tora.paint(g2d);
		weapon.paint(g2d);
		ui.paint(g2d);
		for (int i = 0; i < collectedTreasure.size(); i++) {
			collectedTreasure.get(i).paint(g2d);
		}
		bigChest.paint(g2d);
		g.setColor(Color.blue);
		g.fillRect(600, 50, tora.health * 10, 10);
		g.setColor(Color.black);
		g.fillRect(600 + tora.health * 10, 50, (10 - tora.health) * 10, 10);
	}

	public static void main(String[] args) throws InterruptedException {
		int finalwidth = framewidth;
		int finalheight = frameheight;
		JFrame frame = new JFrame("Tiger! Tiger!");
		Game game = new Game();
		game.maptype = "default";
		frame.add(game);
		// frame.setSize(finalwidth, finalheight);
		frame.setUndecorated(false);
		frame.setBackground(new Color(0, 0, 0));
		game.setPreferredSize(new Dimension(finalwidth, finalheight));
		frame.setResizable(false);
		frame.pack();
		frame.setVisible(true);
		frame.validate();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Map.createMap();
		System.out.print(frame.getContentPane().getSize());
		playSound("TigerTigerdown.wav", "bgm");
		Thread.sleep(1000);
		while (gameStatus == "playing") {
			animationcounter += 1;
			if(animationcounter == 20) {
				animationcounter = 0;
			}
			game.move();
			tora.up = true;
			tora.down = true;
			tora.left = true;
			tora.right = true;
			game.update();
			Camera.update();
			game.repaint();
			Thread.sleep(25);
			// System.out.println((tora.x + Camera.x) + ", " + (tora.y + Camera.y));
			//System.out.println(sounds.size());
		}
	}
}
