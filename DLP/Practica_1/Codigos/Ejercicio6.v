module Ejercicio6(
    // --- Entradas de Control ---
    input  wire record_switch,     // Interruptor para activar la grabación
    input  wire play_switch,       // Interruptor para activar la reproducción
    
    // --- Salidas de Estado ---
    // Deben ser 'reg' porque se asignan dentro de un bloque 'always'
    output reg  record_output,     
    output reg  play_output        
);

    // Bloque que se ejecuta siempre que una de las entradas cambie
    always @(*) begin
        // Lógica para la salida de grabación
        if (record_switch == 0) begin
            record_output = 1;
        end else begin
            record_output = 0;
        end

        // Lógica para la salida de reproducción
        if (play_switch == 0) begin
            play_output = 1;
        end else begin
            play_output = 0;
        end
    end

endmodule