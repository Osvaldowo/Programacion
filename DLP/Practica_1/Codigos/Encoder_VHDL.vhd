library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity Encoder_VHDL is
    port (
        -- Entradas de Reloj y Reset
        clk     : in  std_logic;
        reset   : in  std_logic;

        -- Pines del Encoder
        clk_pin : in  std_logic;              -- Pin CLK (A) del encoder
        dt_pin  : in  std_logic;              -- Pin DT (B) del encoder
        sw_pin  : in  std_logic;              -- Pin SW (Switch/Botón) del encoder

        -- Salidas
        cout    : out std_logic_vector(7 downto 0)  -- Salida del contador
    );
end entity Encoder_VHDL;

architecture Behavioral of Encoder_VHDL is

    -- Señales internas para Sincronización y Antirrebote (Debouncing)
    signal clk_sync : std_logic_vector(1 downto 0) := "00";
    signal dt_sync  : std_logic_vector(1 downto 0) := "00";
    signal sw_sync  : std_logic_vector(1 downto 0) := "00";

    -- Contador principal
    signal count_value : unsigned(7 downto 0) := (others => '0');

begin

    -- P1: Proceso de Sincronización y Antirrebote
    process (clk) is
    begin
        if rising_edge(clk) then
            clk_sync <= clk_sync(0) & clk_pin;
            dt_sync  <= dt_sync(0) & dt_pin;
            sw_sync  <= sw_sync(0) & sw_pin;
        end if;
    end process;


    -- P2: Proceso de Detección de Giro y Control del Contador
    process (clk) is
    begin
        if rising_edge(clk) then
            if reset = '1' then
                count_value <= (others => '0');
            else
                -- Detección de flanco de bajada en CLK
                if clk_sync(1) = '1' and clk_sync(0) = '0' then
                    -- Lógica de giro
                    if dt_sync(0) /= clk_sync(0) then
                        count_value <= count_value + 1;
                    else
                        count_value <= count_value - 1;
                    end if;
                end if;

                -- Lógica del Pulsador SW (Reset del contador)
                if sw_sync(1) = '1' and sw_sync(0) = '0' then
                    count_value <= (others => '0');
                end if;
            end if;
        end if;
    end process;

    -- Asignación de la Salida
    cout <= std_logic_vector(count_value);

end architecture Behavioral;