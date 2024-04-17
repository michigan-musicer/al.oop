public class Square implements Shape {
    private int side;
    public Square(int sideIn) { side = sideIn; }
    public String getShapeType() { return "Square"; }
    public int getPerimeter() { return side * 4; }
    public int getArea() { return side * side; }
}
