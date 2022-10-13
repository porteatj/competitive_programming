import java.util.*;
import java.io.*;
public class Bicol_Problem_Number_4 {
    Map<String, Map> todo_inf = new HashMap<>();
    public static void main(String[] args)throws FileNotFoundException
    {
        Map<String, Map> todo_inf = new HashMap<>();
        // Scanner sc = new Scanner(System.in);
        Map<String, Map> pre_set = todo_inf;
        Scanner sc = new Scanner(new File("prob4.in"));
        while(sc.hasNext())
        {
            String todo = sc.nextLine();
            
            String command = todo.substring(0, todo.indexOf(' ', 0));
            // System.out.println(new_key);
            // System.out.println(command);

            if(command.equals("set-top"))
            {
                pre_set = todo_inf;
            }
            else if(command.equals("goto"))
            {
                String new_key = todo.substring(todo.indexOf(' ', 0)+1);
                pre_set = (Map<String, Map>)pre_set.get(new_key);
            }
            else if(command.equals("set"))
            {
                String new_key = todo.substring(todo.indexOf(' ', 0)+1);
                pre_set.put(new_key, new HashMap<>());
            }
        }
        for(String key : todo_inf.keySet())
        {
            System.out.println(key);
        }
        
    }

    
}
