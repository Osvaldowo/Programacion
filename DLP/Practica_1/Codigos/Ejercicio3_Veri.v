module Ejercicio3_Veri(
    input  wire clk,
    input  wire reset_btn,   // botón (activo en bajo)
    input  wire start_sw,    // switch: 1 = contar, 0 = pausa
    input  wire dir_sw,      // switch: 1 = ascendente, 0 = descendente
    output reg  [7:0] segments, // A-G + DP
    output wire [3:0] digit_en  // activación de dígito
);

    // Contador hexadecimal
    reg [3:0] hex_counter = 4'd0;

    // Divisor de reloj
    reg [23:0] clk_div = 24'd0;
    reg slow_clk = 1'b0;

    // Activar solo el primer dígito (ánodo común, activo en bajo)
    assign digit_en = 4'b1110;

    // Divisor de reloj (~0.5s si clk = 50 MHz)
    always @(posedge clk) begin
        clk_div <= clk_div + 1;
        if (clk_div == 24'd0)
            slow_clk <= ~slow_clk;
    end

    // Proceso principal: contador con control de reset/start/dir
    always @(posedge slow_clk) begin
        if (reset_btn == 1'b0) begin
            hex_counter <= 4'd0;
        end else if (start_sw == 1'b0) begin  // 0 = contar
            if (dir_sw == 1'b1) begin
                // Ascendente
                if (hex_counter == 4'd15)
                    hex_counter <= 4'd0;
                else
                    hex_counter <= hex_counter + 1;
            end else begin
                // Descendente
                if (hex_counter == 4'd0)
                    hex_counter <= 4'd15;
                else
                    hex_counter <= hex_counter - 1;
            end
        end
    end

    // Tabla de segmentos
    always @(*) begin
        case (hex_counter)
            4'd0:  segments = 8'b01000000;
            4'd1:  segments = 8'b01111001;
            4'd2:  segments = 8'b00100100;
            4'd3:  segments = 8'b00110000;
            4'd4:  segments = 8'b00011001;
            4'd5:  segments = 8'b00010010;
            4'd6:  segments = 8'b00000010;
            4'd7:  segments = 8'b01111000;
            4'd8:  segments = 8'b00000000;
            4'd9:  segments = 8'b00010000;
            4'd10: segments = 8'b00001000; // A
            4'd11: segments = 8'b00000011; // B
            4'd12: segments = 8'b01000110; // C
            4'd13: segments = 8'b00100001; // D
            4'd14: segments = 8'b00000110; // E
            4'd15: segments = 8'b00001110; // F
            default: segments = 8'b11111111;
        endcase
    end

endmodule
