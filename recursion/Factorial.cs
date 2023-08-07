namespace Main
{
    public class Factorial
    {
        public void start()
        {
            int value = helper(6);
            Console.WriteLine("Factorial is : {0}", value);
        }

        private int helper(int n)
        {
            if (n == 1)
                return 1;
            
            return n * helper(n-1);

        }
    }
}