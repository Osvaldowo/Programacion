library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Recep is
Port ( 
    clk,rst,rx: in std_logic;
    leds: out std_logic_vector(7 downto 0)
);
end Recep;

architecture Arq_Recep of Recep is
    signal erx: std_logic:='0';
    signal trx_us: UNSIGNED(4 downto 0) := (others => '0'); 
    signal regrx: std_logic_vector(7 downto 0):="00000000";
    
   
    signal cntrx_us: UNSIGNED(10 downto 0) := (others => '0'); 
    

    constant BAUD_3X_C : STD_LOGIC_VECTOR(10 downto 0):="11011001000"; -- 1736 en binario
    constant BAUD_3X_US : UNSIGNED(10 downto 0) := to_unsigned(1735, 11); -- 1736-1 para la comparación
    
    signal trx: std_logic_vector(4 downto 0); -- Se mantiene para las condiciones de captura
begin
    -- Asignación para las condiciones de captura
    trx <= STD_LOGIC_VECTOR(trx_us);

    -- Habilita la recepción al detectar el bit de inicio
    process (rst, rx)
    begin
        if rst='1' then
            erx <= '0';
        elsif rx='0' and erx = '0' then 
            erx <= '1';
        elsif trx_us = to_unsigned(27, 5) then 
            erx <= '0'; 
        else null;
        end if;
    end process;

    -- Conteo para el tiempo del receptor
    process (clk, rst)
    begin
        if (rst='1' or erx='0') then
            cntrx_us <= (others=>'0');
            trx_us <= (others=>'0');
        elsif (rising_edge(clk) and erx='1') then
            if (cntrx_us = BAUD_3X_US) then 
                trx_us <= trx_us + 1;
                cntrx_us <= (others=>'0');
            else
                cntrx_us <= cntrx_us + 1;
            end if;
        end if;
    end process;
    
    -- Recibe los datos en el registro del receptor regrx
    process (clk, rst)
    begin
        if rst='1' then
            regrx <= (others=>'0');
            leds <= (others=>'0');
        elsif (rising_edge(clk)) then
            case (trx) is -- captura en el centro del bit:
            when "00100" => regrx(0) <= rx; -- 4 (inicio del bit 0)
            when "00111" => regrx(1) <= rx; -- 7
            when "01010" => regrx(2) <= rx; -- 10
            when "01101" => regrx(3) <= rx; -- 13
            when "10000" => regrx(4) <= rx; -- 16
            when "10011" => regrx(5) <= rx; -- 19
            when "10110" => regrx(6) <= rx; -- 22
            when "11001" => regrx(7) <= rx; -- 25
            when "11010" => leds <= regrx; -- 26 Carga el dato a leds
            when others => null;
            end case;
        end if;
    end process;
end Arq_Recep;