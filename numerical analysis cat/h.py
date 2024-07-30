# x = [1 2 3 4 5 6];
# y = [-5.5 43.1 128 290.7 498.4 978.67];
# p = polyfit(x, y, 4);
# x2 = 1:0.1:6;
# y2 = polyval(p, x2);
# plot(x, y, 'o', x2, y2);
# grid on

'''
    The `polyfit` function fits a polynomial of degree 4 to the data points `(x, y)`, 
    and returns the coefficients of the polynomial. 
    The `polyval` function evaluates the polynomial at the points `x2`, 
    and the `plot` function is used to plot the original data points `(x, y)` as circles and the fitted polynomial curve `(x2, y2)`.
    
'''