
// Adapted from https://introcs.cs.princeton.edu/java/32class/ColorJulia.java.html
// mandel.txt is taken from exercise 35 on https://introcs.cs.princeton.edu/java/32class/

/******************************************************************************
 *  Compilation:  javac ColorJulia.java
 *  Execution:    java ColorJulia a b < file.txt
 *  Dependencies: Picture.java
 *
 *  Plots the Julia for the complex point c = a + ib.
 *
 *  The set of points in the Julia set is connected if and only if
 *  c is in the Mandelbrot set.
 *
 *  % java ColorJulia -0.75 0.1 < mandel.txt
 *
 *  % java ColorJulia -1.25 0 < mandel.txt
 *
 *  % java ColorJulia 0.1 0.7 < mandel.txt
 *
 ******************************************************************************/

import java.awt.*;
import java.util.Scanner;

public class JuliaSolution
{


    // return number of iterations to check z is in the Julia set of c
    static int julia(Complex c, Complex z, int maximumIterations)
    {
        for (int t = 0; t < maximumIterations; t++)
        {
            if (z.abs() > 2.0) return t;
            z = z.times(z).plus(c);
        }
        return maximumIterations - 1;
    }


    public static void main(String[] args)
    {
        /**
         * TODO: read in real, imag, n, and ITERS as command line arguments.
         * Use the Mandelbrot example if you aren't sure how to do this.
         */
        double real = Double.parseDouble(args[0]);      // a
        double imag = Double.parseDouble(args[1]);      // b
        int n = 512;
        int ITERS = 256;
//        end solution
        Complex c = new Complex(real, imag);            // c = a + ib
        double xmin = -2.0;
        double ymin = -2.0;
        double width = 4.0;
        double height = 4.0;

        Scanner input = new Scanner(System.in);

        // read in color map
        Color[] colors = new Color[ITERS];
        /**
         * TODO: read in colors from input.
         * The input object reads in from the file redirection we set up. It has a method called nextInt
         * that you can call to read in the next value from the input.
         * You should set each value in colors to a corresponding RGB value from the input file.
         * If you get stuck, print using System.out.println to help you debug!
         */
        for (int t = 0; t < ITERS; t++)
        {
            int r = input.nextInt();
            int g = input.nextInt();
            int b = input.nextInt();
            colors[t] = new Color(r, g, b);
        }
        // end

//        Challenge #1: move everything into a file. Put initial parameters in and then list all colors.
//        Challenge #2: zoom in on the center however many times: fix n (the size) and then create i different zoom-ins
//        where i is another parameter passed into the program arguments. This means creating i different Picture objects
//        with different zoom levels - see Mandelbrot class for how to implement.
        Picture picture = new Picture(n, n);

        for (int col = 0; col < n; col++)
        {
            for (int row = 0; row < n; row++)
            {
                double x = xmin + col * width / n;
                double y = ymin + row * height / n;
                Complex z = new Complex(x, y);
                int t = julia(c, z, ITERS);
                picture.set(col, n - 1 - row, colors[t]);
            }
        }
        picture.show();
    }
}



//Copyright © 2000–2022, Robert Sedgewick and Kevin Wayne.
//Last updated: Thu Aug 11 10:22:50 EDT 2022.