//import javax.swing.*;
//import java.awt.*;
//import java.util.Stack;
//
//// A ChatGPT-generated TowersOfHanoi example.
//public class TowersOfHanoi extends JPanel {
//    private int numDisks;
//    private Stack<Integer>[] towers;
//    private final Color[] diskColors = {Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW, Color.ORANGE};
//
//    public TowersOfHanoi(int numDisks) {
//        this.numDisks = numDisks;
//        towers = new Stack[3];
//        for (int i = 0; i < 3; i++) {
//            towers[i] = new Stack<>();
//        }
//        for (int i = numDisks; i > 0; i--) {
//            towers[0].push(i);
//        }
//    }
//
//    @Override
//    protected void paintComponent(Graphics g) {
//        super.paintComponent(g);
//        int towerWidth = getWidth() / 4;
//        int diskHeight = getHeight() / (numDisks + 1);
//
//        for (int i = 0; i < 3; i++) {
//            int x = (i + 1) * towerWidth;
//            int y = getHeight();
//            g.setColor(Color.BLACK);
//            g.fillRect(x - 5, 0, 10, getHeight());
//            Stack<Integer> tower = towers[i];
//            for (int j = 0; j < tower.size(); j++) {
//                int disk = tower.get(j);
//                g.setColor(diskColors[disk - 1]);
//                int diskWidth = disk * towerWidth / (numDisks + 1);
//                g.fillRect(x - diskWidth / 2, y - diskHeight, diskWidth, diskHeight);
//                y -= diskHeight;
//            }
//        }
//    }
//
//    private void moveTower(int disks, int from, int to, int via) {
//        if (disks == 1) {
//            towers[to].push(towers[from].pop());
//            repaint();
//        } else {
//            moveTower(disks - 1, from, via, to);
//            moveTower(1, from, to, via);
//            moveTower(disks - 1, via, to, from);
//        }
//    }
//
//    public void solve() {
//        moveTower(numDisks, 0, 2, 1);
//    }
//
//    public static void main(String[] args) {
//        int numDisks = 5;
//        TowersOfHanoi towerOfHanoi = new TowersOfHanoi(numDisks);
//        JFrame frame = new JFrame("Tower of Hanoi");
//        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        frame.add(towerOfHanoi);
//        frame.setSize(800, 600);
//        frame.setLocationRelativeTo(null);
//        frame.setVisible(true);
//        towerOfHanoi.solve();
//    }
//}