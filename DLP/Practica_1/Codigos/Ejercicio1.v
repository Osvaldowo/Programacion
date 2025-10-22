module Ejercicio1(
    // Entradas
    input A,
    input B,
    input C,
    
    // Salidas
    output reg S1,
    output reg S2,
    output reg S3,
    output reg S4,
    output reg S5,
    output reg S6
);

    // Invertir entradas
    wire a, b, c;
    assign a = ~A;
    assign b = ~B;
    assign c = ~C;


    always @(*) begin
        // Ahora toda la lógica usa las señales invertidas (a_in, b_in, c_in)
        
        // Lógica para S1 (001, 010, 100, 111)
        S1 = (~a & ~b &  c) | (~a &  b & ~c) | ( a & ~b & ~c) | ( a &  b &  c);
        
        // Lógica para S2 (todas menos 000)
        S2 = a | b | c;
        
        // Lógica para S3
        S3 = (~a & ~b) | (a & b);
        
        // Lógica para S4 (001, 011, 101)
        S4 = (~a & b & c) | (a & b & ~c) ;
        
        // Lógica para S5 (000, 011, 100, 111)
        S5 = ~a & ~b & ~c;
        
        // Lógica para S6 (010, 100, 101)
        S6 = a & ~c;
    end

endmodule