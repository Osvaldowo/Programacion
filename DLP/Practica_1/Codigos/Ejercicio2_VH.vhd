library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Ejercicio2_VH is
    Port (
        clk    : in  std_logic;           -- reloj de la FPGA (ej. 50 MHz)
        dipsw  : in  std_logic_vector(7 downto 0); -- DIP switches de 8 bits
        leds   : out std_logic_vector(7 downto 0)  -- LEDs de 8 bits
    );
end Ejercicio2_VH;

architecture Behavioral of Ejercicio2_VH is


    signal clk_div  : unsigned(23 downto 0) := (others => '0');  -- contador 24 bits
    signal slow_clk : std_logic := '0';

    signal reg_d : std_logic_vector(7 downto 0) := (others => '0');

begin

    -- Divisor de reloj: cada flanco de clk incrementa clk_div
    process(clk)
    begin
        if rising_edge(clk) then
            clk_div <= clk_div + 1;
            slow_clk <= clk_div(23);  -- bit más alto del contador
        end if;
    end process;

    -- Registro tipo D: captura los DIP switches al flanco de slow_clk
    process(slow_clk)
    begin
        if rising_edge(slow_clk) then
            reg_d <= dipsw;
        end if;
    end process;

    -- Salida a LEDs
    leds <= reg_d;

end Behavioral;
