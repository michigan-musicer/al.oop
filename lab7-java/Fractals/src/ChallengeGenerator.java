import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

import static java.lang.String.format;

public class ChallengeGenerator
{
    public static void main(String[] args) throws IOException
    {
        Random rand = new Random();
        ArrayList<String> stringList = new ArrayList<>();
        for (int i = 0; i < 512; ++i)
        {
            stringList.addLast(format("%d %d %d", rand.nextInt(255), rand.nextInt(255), rand.nextInt(255)));
        }
        FileWriter fileWriter = new FileWriter("mandel_challenge.txt");
        for (String str : stringList) {
            fileWriter.write(str + System.lineSeparator());
        }
        fileWriter.close();
    }
}
