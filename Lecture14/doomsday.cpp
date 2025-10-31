int main()
{
    while (true)
    {
        // This uses up 4 bytes of memory, in a loop: 4*infinity
        double *opptatt_minne = new double();

        // This frees all the allocated memory above
        delete opptatt_minne;
    }
}
