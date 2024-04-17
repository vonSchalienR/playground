package HARJTYÖjava;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class game extends JPanel implements ActionListener, KeyListener {
    private Timer timer;
    private int objektinY;
    private int hyppy;
    private int esteenX, esteenY, esteenLeveys, esteenKorkeus;
    private boolean peliKaynnissa;

    public game() {
        this.setPreferredSize(new Dimension(800, 600));
        this.setBackground(Color.WHITE);
        this.setFocusable(true);
        this.addKeyListener(this);

        objektinY = 400;
        hyppy = 0;
        esteenX = 800;
        esteenY = 380;
        esteenLeveys = 50;
        esteenKorkeus = 50;
        peliKaynnissa = true;

        timer = new Timer(50, this);
        timer.start();
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        g.setColor(Color.ORANGE);
        g.fillRect(100, objektinY, 50, 50); // objekti

        g.setColor(Color.PINK);
        g.fillRect(esteenX, esteenY, esteenLeveys, esteenKorkeus); // este

      
           
    }

    public void actionPerformed(ActionEvent e) {
        if (peliKaynnissa) {
            esteenX -= 5;
            if (esteenX < -esteenLeveys) {
                esteenX = 800;
            }

            if (hyppy > 0) {
                objektinY -= hyppy;
                hyppy -= 1;
            }

            if (objektinY >= 400) {
                objektinY = 400;
                hyppy = 0;
            }

            if (objektinY < 0) {
                objektinY = 0;
                hyppy = 0;
            }

            if (esteenX < 150 && objektinY + 50 >= esteenY) {
                peliKaynnissa = false;
            }

            repaint();
        }
    }

    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();
        if (key == KeyEvent.VK_SPACE) {
            hyppy = 15;
        } else if (key == KeyEvent.VK_UP) {
            liikuYlos();
        } else if (key == KeyEvent.VK_DOWN) {
            liikuAlas();
        }
    }

    public void keyTyped(KeyEvent e) {
    }

    public void keyReleased(KeyEvent e) {
    }

    private void liikuYlos() {
        if (objektinY > 0) {
            objektinY -= 5;
        }
    }

    private void liikuAlas() {
        if (objektinY < 550) {
            objektinY += 5;
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("GAME ON BITCH");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
        frame.setLayout(new BorderLayout());
        frame.add(new game(), BorderLayout.CENTER);
        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
