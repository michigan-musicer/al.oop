import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Stack;

// A ChatGPT-generated TowersOfHanoi example.
public class TowersOfHanoiCompleted extends JPanel {
    private int numDisks;
    private Stack<Integer>[] towers;
    private final Color[] diskColors = {Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.ORANGE};

    public TowersOfHanoiCompleted(int numDisks) {
        this.numDisks = numDisks;
        towers = new Stack[3];
        for (int i = 0; i < 3; i++) {
            towers[i] = new Stack<>();
        }
        for (int i = numDisks; i > 0; i--) {
            towers[0].push(i);
        }

        setPreferredSize(new Dimension(1200, 800));
    }

//    TASK 1: reset TowersOfHanoiCompleted to its initial state.
//    We consider the state of towersOfHanoiCompleted to be reset when
//    all disks are on the FIRST tower.
//    Note that this demonstrates private vs public members - we can't do this
//    directly within construction of the reset button.
    public void reset() {
//        Your code goes here.
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        int towerWidth = getWidth() / 4;
        int diskHeight = getHeight() / (numDisks + 1);

        for (int i = 0; i < 3; i++) {
            int x = (i + 1) * towerWidth;
            int y = getHeight();
            g.setColor(Color.BLACK);
            g.fillRect(x - 5, 0, 10, getHeight());
            Stack<Integer> tower = towers[i];
            for (int j = 0; j < tower.size(); j++) {
                int disk = tower.get(j);
                g.setColor(diskColors[disk - 1]);
                int diskWidth = disk * towerWidth / (numDisks + 1);
                g.fillRect(x - diskWidth / 2, y - diskHeight, diskWidth, diskHeight);
                y -= diskHeight;
            }
        }
    }

    private void moveTower(int disks, int from, int to, int via) {
        // do a short pause to make sure we can actually see stuff happen.
        try {
            Thread.sleep(500);
        }
        catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        if (disks == 1) {
            towers[to].push(towers[from].pop());
            update(getGraphics());
        } else {
            moveTower(disks - 1, from, via, to);
            moveTower(1, from, to, via);
            moveTower(disks - 1, via, to, from);
        }
    }

    private void solve() {
        moveTower(numDisks, 0, 2, 1);
    }

// TASK 2: add button that runs solve() when clicked.
    private static void addSolveButton(JPanel panel, TowersOfHanoiCompleted towersOfHanoi) {
        // Your code goes here.
        // You will need to create a new JButton object and add it to the panel.
        // The JButton object also needs to implement an ActionListener that calls solve()
        // on the towersOfHanoi object passed into the function.
    }

// TASK 3: add button that resets class to initial state when clicked.
//    We consider the state of towersOfHanoiCompleted to be reset when
//    all disks are on the FIRST tower.
    private static void addResetButton(JPanel panel, TowersOfHanoiCompleted towersOfHanoi) {
        // Your code goes here.
        // You will need to create a new JButton object and add it to the panel.
        // The JButton object also needs to implement an ActionListener that calls reset()
        // on the towersOfHanoi object passed into the function.
    }

    public static void main(String[] args) {
        int numDisks = 5;
        TowersOfHanoiCompleted towerOfHanoi = new TowersOfHanoiCompleted(numDisks);
        JFrame frame = new JFrame("Tower of Hanoi");
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS));

        JPanel topPanel = new JPanel();
        JPanel bottomPanel = new JPanel();

        topPanel.add(towerOfHanoi);
        topPanel.setSize(new Dimension(1200, 800));
        addSolveButton(bottomPanel, towerOfHanoi);
        addResetButton(bottomPanel, towerOfHanoi);
        mainPanel.add(topPanel);
        mainPanel.add(bottomPanel);
        frame.add(mainPanel);


        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1200, 900);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
