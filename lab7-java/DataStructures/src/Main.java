public class Main
{
    public static void main(String[] args)
    {
        VectorCustom<Integer> intV = new VectorCustom<>();
        System.out.println(intV.empty());
        intV.pushBack(1);
        intV.pushBack(2);
        intV.pushBack(3);
        System.out.println(intV.size());
        System.out.println(intV.get(0));
        System.out.println(intV.get(1));
        System.out.println(intV.get(2));
        System.out.println(intV.popFront());
        System.out.println(intV.size());
        System.out.println(intV.get(0));
        System.out.println(intV.get(1));

        VectorCustom<String> stringV = new VectorCustom<>();
        stringV.pushBack("hello");
        stringV.pushBack("my");
        stringV.pushBack("name");
        stringV.pushBack("is");
        stringV.pushBack("Ryan");
        for (int i = 0; i < stringV.size(); ++i)
        {
            System.out.println(stringV.get(i) + " ");
        }
    }
}
