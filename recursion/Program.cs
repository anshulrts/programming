﻿using System;
using MinMaxNamespace;

namespace Main
{
    class Program
    {
        static void Main(string[] args)
        {
            while(true)
            {
                Console.WriteLine("0. Exit");
                Console.WriteLine("1. Factorial");
                Console.WriteLine("2. Max-Min");
                
                Console.WriteLine("\nEnter Choice");
                string x = Console.ReadLine();

                switch(Convert.ToInt32(x))
                {
                    case 0: Environment.Exit(0); break;
                    default: break;

                    case 1:
                    Factorial f = new Factorial();
                    f.start();
                    break;

                    case 2:
                    MinMax mm = new MinMax();
                    mm.start();
                    break;
                }
            }
        }
    }
}