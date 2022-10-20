int main(void) {    
    double actual_pi = 3.141592653589793238462643;
    int n;
    double calc_pi = 0.0, *part_sum , *dev_part_sum;

    printf("The pi calculator. \n");
    printf("Intervals");

    scanf("%d", &n);
    if (n == 0) break;

    malloc((void**) &part_sum, n * sizeof(double));
    cudaMalloc((void**) &dev_part_sum, n * sizeof(double));
    
    term<<<1, n>>>(dev_part_sum); // 1 block, n threads

    cudaMemcpy(part_sum, dev_part_sum, n * sizeof(double), cudaMemcpyDeviceToHost);

    for (int i = 0; i < n; i ++) calc_pi += part_sum[i];

    cudaFree(dev_part_sum);
    free(part_sum);

    printf("pi = %f n", calc_pi);
    printf("Error = %f n", fabs(calc_pi - actual_pi));
}