module Ejercicio4 #(parameter N = 24)(
    input clk,       // Reloj del FPGA (ej: 50 MHz)
    input enc,       // Encendido/apagado de la sirena
    input des,       // Selector: 1 = policía, 0 = ambulancia
    output reg sal   // Salida a la bocina
);

    parameter POLICE_FREQ1 = 30000;   // tono 1 policía
    parameter POLICE_FREQ2 = 50000;   // tono 2 policía
    parameter AMB_MIN = 20000;       // rango ambulancia
    parameter AMB_MAX = 60000;
    parameter STEP    = 50;          // paso de barrido ambulancia
    parameter TOGGLE_TIME = 50_000_000; 
    // Con clk=50 MHz → 100M ciclos ≈ 2 s

    reg [N-1:0] div_cnt = 0;     
    reg [31:0] time_cnt = 0;     // contador para intervalos largos
    reg [15:0] tone_freq = POLICE_FREQ1;
    reg dir = 1;                 // Dirección barrido ambulancia
    reg police_sel = 0;          // Alterna tono policía

    always @(posedge clk) begin
        if (!enc) begin
            sal <= 0;  
            div_cnt <= 0;
            time_cnt <= 0;
            tone_freq <= POLICE_FREQ1;
            police_sel <= 0;
        end else begin
            if (des) begin
                //  Sirena de policía (dos tonos conmutados cada 2 s)
                if (div_cnt >= tone_freq) begin
                    sal <= ~sal;
                    div_cnt <= 0;
                end else begin
                    div_cnt <= div_cnt + 1;
                end

                // Contador de 2 segundos
                if (time_cnt >= TOGGLE_TIME) begin
                    time_cnt <= 0;
                    police_sel <= ~police_sel;
                    if (police_sel)
                        tone_freq <= POLICE_FREQ1;
                    else
                        tone_freq <= POLICE_FREQ2;
                end else begin
                    time_cnt <= time_cnt + 1;
                end

            end else begin
                // Sirena de ambulancia (barrido asc/desc)
                if (div_cnt >= tone_freq) begin
                    sal <= ~sal;
                    div_cnt <= 0;
                end else begin
                    div_cnt <= div_cnt + 1;
                end

                if (div_cnt == 0) begin
                    if (dir)
                        tone_freq <= tone_freq - STEP; // sube
                    else
                        tone_freq <= tone_freq + STEP; // baja
                    
                    if (tone_freq < AMB_MIN) dir <= 0;
                    if (tone_freq > AMB_MAX) dir <= 1;
                end
            end
        end
    end
endmodule
