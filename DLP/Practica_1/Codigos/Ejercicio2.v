module Ejercicio2(
    input  wire       clk,         // reloj de la FPGA (50 MHz)
    input  wire       btn_captura, // NUEVA entrada para el botón
    input  wire [7:0] dipsw,       // DIP switches de 8 bits
    output reg  [7:0] leds = 8'd0   // LEDs de 8 bits, inicializados en 0
);

    reg [1:0] btn_sincronizador;
    wire      pulso_captura;

    always @(posedge clk) begin
      // Sincronizamos el botón con el reloj del sistema para evitar errores
      btn_sincronizador <= {btn_sincronizador[0], btn_captura};
    end

    // Genera un pulso cuando el botón pasa de '0' a '1' (se presiona)
    assign pulso_captura = btn_sincronizador[1] & ~btn_sincronizador[0];

    always @(posedge clk) begin
        if (pulso_captura) begin
            leds <= dipsw; // Capturamos el valor de los switches en los LEDs.
        end
        // Si no hay pulso, 'leds' mantiene su valor anterior (comportamiento de memoria).
    end

endmodule