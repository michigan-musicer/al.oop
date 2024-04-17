import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Shape> shapes = new ArrayList<>();
        Rectangle r1 = new Rectangle(3, 4);
        Rectangle r2 = new Rectangle(5, 5);
//      Task 3: create two Triangle objects named t1 and t2.
//      t1 should have side lenghts 4, 4, 4, and t2 should have
//      side lengths 5, 3, 4.

        shapes.add(r1);
        shapes.add(r2);
        shapes.add(t1);
        shapes.add(t2);

//      When running the code below, t1 should have a perimeter of 12 and an area of about 6.93.
//      t2 should have a perimeter of 12 and an area of exactly 6.

        for (Shape shape : shapes)
        {
            System.out.println("Shape type: " + shape.getShapeType());
            System.out.println("Shape perimeter: " + Integer.toString(shape.getPerimeter()));
            System.out.println("Shape area: " + Integer.toString(shape.getArea()));
        }
    }
}