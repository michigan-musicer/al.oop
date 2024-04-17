public class TriangleSolution implements Shape {
    private int side1;
    private int side2;
    private int side3;
    public TriangleSolution(int side1In, int side2In, int side3In)
    {
        side1 = side1In;
        side2 = side2In;
        side3 = side3In;
    }

    @Override
    public String getShapeType()
    {
        return "Triangle";
    }

    @Override
    public int getPerimeter() {
        return side1 + side2 + side3;
    }

    @Override
    public int getArea() {
        return (int)Math.sqrt((side1 + side2 + side3) * (-side1 + side2 + side3) * (side1 - side2 + side3) * (side1 + side2 - side3) / 4);
    }
}
