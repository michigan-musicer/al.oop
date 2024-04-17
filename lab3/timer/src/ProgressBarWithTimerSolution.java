import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.beans.*;
import java.util.Random;

// Task 4: complete ProgressBarWithTimer by completing the sections marked YOUR CODE HERE, following the instructions.
// Reference this document: https://docs.oracle.com/javase%2Ftutorial%2F/uiswing/components/progress.html

// Most of the source is taken directly from https://docs.oracle.com/javase%2Ftutorial%2F/uiswing/examples/components/ProgressBarDemoProject/src/components/ProgressBarDemo.java.
// However, you are asked to implement a different task that makes progress based on Timer rather than
// random number generation as in the original source.
public class ProgressBarWithTimerSolution extends JPanel implements ActionListener, PropertyChangeListener {
    // YOUR CODE HERE: add a private JProgressBar object member called progressBar.
    private JProgressBar progressBar;
    // END OF SECTION
    private JButton startButton;
    private JTextArea taskOutput;
    private Task task;

    class MyTimer
    {
        private long currentTime;
        public MyTimer()
        {
            this.currentTime = System.nanoTime();
        }

        // This will be a very rough implementation that is inexact and would not be suitable for
        // very precise applications, e.g. critical embedded systems in a vehicle.
        public long resetAndGetDifference()
        {
            // YOUR CODE HERE: update currentTime and return the difference between the previous value of
            // currentTime and the current system time.
            // NOTE: it will be easiest if you return the time difference in tenths of a second
            // instead of in nanoseconds.
            long difference = (System.nanoTime() - this.currentTime) / 1000000;
            this.currentTime = System.nanoTime();
            return difference;
            // END OF SECTION
        }

    }

    class Task extends SwingWorker<Void, Void> {
        /*
         * Main task. Executed in background thread.
         */
        @Override
        public Void doInBackground() {
            Random random = new Random();
            int progress = 0;
            //Initialize progress property.
            setProgress(0);
            // YOUR CODE HERE: construct a MyTimer object.
            MyTimer timer = new MyTimer();
            // END OF SECTION
            while (progress < 100) {
                //Sleep for up to one second.
                try {
                    Thread.sleep(random.nextInt(1000));
                } catch (InterruptedException ignore) {}
                // YOUR CODE HERE: make a deterministic amount of progress based on Timer.
                progress += timer.resetAndGetDifference() / 100;
                System.out.println(progress);
                // END SECTION
                setProgress(Math.min(progress, 100));
            }
            return null;
        }

        /*
         * Executed in event dispatching thread
         */
        @Override
        public void done() {
            Toolkit.getDefaultToolkit().beep();
            startButton.setEnabled(true);
            setCursor(null); //turn off the wait cursor
            taskOutput.append("Done!\n");
        }
    }

    public ProgressBarWithTimerSolution()
    {
        super(new BorderLayout());

        // Create the demo's UI.
        startButton = new JButton("Start");
        startButton.setActionCommand("start");
        startButton.addActionListener(this);

        // YOUR CODE HERE: construct progressBar.
        progressBar = new JProgressBar(0, 100);
        progressBar.setValue(0);
        progressBar.setStringPainted(true);
        // END OF SECTION

        taskOutput = new JTextArea(5, 20);
        taskOutput.setMargin(new Insets(5,5,5,5));
        taskOutput.setEditable(false);

        JPanel panel = new JPanel();
        panel.add(startButton);
        panel.add(progressBar);

        add(panel, BorderLayout.PAGE_START);
        add(new JScrollPane(taskOutput), BorderLayout.CENTER);
        setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
    }

    public void actionPerformed(ActionEvent evt)
    {
        startButton.setEnabled(false);
        setCursor(Cursor.getPredefinedCursor(Cursor.WAIT_CURSOR));
        task = new Task();
        task.addPropertyChangeListener(this);
        task.execute();
    }

    public void propertyChange(PropertyChangeEvent evt)
    {
        if ("progress" == evt.getPropertyName())
        {
            int progress = (Integer) evt.getNewValue();
            progressBar.setValue(progress);
            taskOutput.append(String.format(
                    "Completed %d%% of task.\n", task.getProgress()));
        }
    }

    private static void createAndShowGUI()
    {
        //Create and set up the window.
        JFrame frame = new JFrame("ProgressBarDemo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Create and set up the content pane.
        JComponent newContentPane = new ProgressBarWithTimerSolution();
        newContentPane.setOpaque(true); //content panes must be opaque
        frame.setContentPane(newContentPane);

        //Display the window.
        frame.pack();
        frame.setVisible(true);
    }

    public static void main(String[] args)
    {
//      some arbitrary time
        javax.swing.SwingUtilities.invokeLater(new Runnable()
        {
            public void run() {
                createAndShowGUI();
            }
        });

    }
}
