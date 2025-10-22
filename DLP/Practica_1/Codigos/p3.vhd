library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity P3 is
    Port (
        clk         : in  std_logic;
        reset_btn   : in  std_logic;  -- botón
        start_sw    : in  std_logic;  -- switch: 1 = contar, 0 = pausa
        dir_sw      : in  std_logic;  -- switch: 1 = ascendente, 0 = descendente
        segments    : out std_logic_vector(7 downto 0);  -- A-G + DP
        digit_en    : out std_logic_vector(3 downto 0)   -- Activación de dígito
    );
end P3;

architecture Behavioral of P3 is

    signal hex_counter : integer range 0 to 15 := 0;
    signal clk_div     : unsigned(23 downto 0) := (others => '0');
    signal slow_clk    : std_logic := '0';

    -- Tabla de segmentos
    function to_segments(val : integer) return std_logic_vector is
    begin
        case val is
            when 0  => return "01000000";
            when 1  => return "01111001";
            when 2  => return "00100100";
            when 3  => return "00110000";
            when 4  => return "00011001";
            when 5  => return "00010010";
            when 6  => return "00000010";
            when 7  => return "01111000";
            when 8  => return "00000000";
            when 9  => return "00010000";
            when 10 => return "00001000"; -- A
            when 11 => return "00000011"; -- B
            when 12 => return "01000110"; -- C
            when 13 => return "00100001"; -- D
            when 14 => return "00000110"; -- E
            when 15 => return "00001110"; -- F
            when others => return "11111111";
        end case;
    end function;

begin

    -- Activar solo el primer dígito (ánodo común)
    digit_en <= "1110";

    -- Divisor de reloj para generar reloj lento (~0.5s si clk = 50MHz)
    process(clk)
    begin
        if rising_edge(clk) then
            clk_div <= clk_div + 1;
            if clk_div = 0 then
                slow_clk <= not slow_clk;
            end if;
        end if;
    end process;

    -- Proceso principal con control por switches
    process(slow_clk)
    begin
        if rising_edge(slow_clk) then
            if reset_btn = '0' then
                hex_counter <= 0;
            elsif start_sw = '0' then  -- Solo cuenta si el switch está activado
                if dir_sw = '1' then
                    -- Contador ascendente
                    if hex_counter = 15 then
                        hex_counter <= 0;
                    else
                        hex_counter <= hex_counter + 1;
                    end if;
                else
                    -- Contador descendente
                    if hex_counter = 0 then
                        hex_counter <= 15;
                    else
                        hex_counter <= hex_counter - 1;
                    end if;
                end if;
            end if;
        end if;
    end process;

    -- Salida a segmentos
    segments <= to_segments(hex_counter);

end Behavioral;

