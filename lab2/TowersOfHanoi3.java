//import javax.swing.*;
//import java.awt.*;
//import java.awt.event.ActionEvent;
//import java.awt.event.ActionListener;
//
//public class TowersOfHanoi3 extends JFrame {
//    public TowersOfHanoi3() {
//        setTitle("Tower of Hanoi");
//        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        setLayout(new BorderLayout());
//
//        TowerOfHanoi towerOfHanoi = new TowerOfHanoi(5);
//        add(towerOfHanoi, BorderLayout.CENTER);
//
//        JButton solveButton = new JButton("Solve");
//        solveButton.addActionListener(new ActionListener() {
//            @Override
//            public void actionPerformed(ActionEvent e) {
//                towerOfHanoi.solve();
//            }
//        });
//        add(solveButton, BorderLayout.SOUTH);
//
//        pack();
//        setLocationRelativeTo(null);
//    }
//
//    public static void main(String[] args) {
//        SwingUtilities.invokeLater(new Runnable() {
//            @Override
//            public void run() {
//                new TowersOfHanoi3().setVisible(true);
//            }
//        });
//    }
//}
//
//class TowerOfHanoi extends JPanel {
//    private int numDisks;
//    private Tower[] towers;
//
//    public TowerOfHanoi(int numDisks) {
//        this.numDisks = numDisks;
//        towers = new Tower[3];
//        for (int i = 0; i < 3; i++) {
//            towers[i] = new Tower();
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
//                g.setColor(new Color(255 - (tower.size() * 25), 0, 0));
//                int diskWidth = disk * towerWidth / (numDisks + 1);
//                g.fillRect(x - diskWidth / 2, y - diskHeight, diskWidth, diskHeight);
//                y -= diskHeight;
//            }
//        }
//    }
//
//    public void solve() {
//        moveTower(numDisks, 0, 2, 1);
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
//}
//
//class Tower extends Stack<Integer> {
//    // Tower is just a simple Stack<Integer>
//}