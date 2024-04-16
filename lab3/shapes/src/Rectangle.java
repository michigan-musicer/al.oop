public class Rectangle implements Shape {
    private int width;
    private int height;
    public Rectangle(int widthIn, int heightIn)
    {
        width = widthIn;
        height = heightIn;
    }
    public String getShapeType()
    {
        return "Rectangle";
    }
    public int getPerimeter()
    {
        return 2 * width + 2 * height;
    }
    public int getArea()
    {
        return width * height;
    }
}
