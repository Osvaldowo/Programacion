library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Ejercicio4_VH is
    generic (
        N           : integer := 24;
        POLICE_FREQ1: integer := 30000;
        POLICE_FREQ2: integer := 50000;
        AMB_MIN     : integer := 20000;
        AMB_MAX     : integer := 60000;
        STEP        : integer := 50;
        TOGGLE_TIME : integer := 50000000   -- clk=50 MHz -> 2 s
    );
    port(
        clk  : in  std_logic;
        enc  : in  std_logic;
        des  : in  std_logic;   -- 1 = policía, 0 = ambulancia
        sal  : out std_logic
    );
end Ejercicio4_VH;

architecture Behavioral of Ejercicio4_VH is

    signal div_cnt    : unsigned(N-1 downto 0) := (others => '0');
    signal time_cnt   : unsigned(31 downto 0) := (others => '0');
    signal tone_freq  : integer := POLICE_FREQ1;
    signal dir        : std_logic := '1';         -- Dirección del barrido ambulancia
    signal police_sel : std_logic := '0';         -- Alterna tono policía
    signal sal_reg    : std_logic := '0';

begin

    sal <= sal_reg;

    process(clk)
    begin
        if rising_edge(clk) then
            if enc = '0' then
                sal_reg    <= '0';
                div_cnt    <= (others => '0');
                time_cnt   <= (others => '0');
                tone_freq  <= POLICE_FREQ1;
                police_sel <= '0';
                dir        <= '1';
            else
                if des = '1' then
                    -- Sirena de policía
                    if div_cnt >= to_unsigned(tone_freq, N) then
                        sal_reg <= not sal_reg;
                        div_cnt <= (others => '0');
                    else
                        div_cnt <= div_cnt + 1;
                    end if;

                    if time_cnt >= to_unsigned(TOGGLE_TIME, 32) then
                        time_cnt <= (others => '0');
                        police_sel <= not police_sel;
                        if police_sel = '1' then
                            tone_freq <= POLICE_FREQ1;
                        else
                            tone_freq <= POLICE_FREQ2;
                        end if;
                    else
                        time_cnt <= time_cnt + 1;
                    end if;

                else
                    -- Sirena de ambulancia (barrido ascendente/descendente)
                    if div_cnt >= to_unsigned(tone_freq, N) then
                        sal_reg <= not sal_reg;
                        div_cnt <= (others => '0');
                    else
                        div_cnt <= div_cnt + 1;
                    end if;

                    if div_cnt = 0 then
                        if dir = '1' then
                            tone_freq <= tone_freq - STEP;
                        else
                            tone_freq <= tone_freq + STEP;
                        end if;

                        if tone_freq < AMB_MIN then
                            dir <= '0';
                        elsif tone_freq > AMB_MAX then
                            dir <= '1';
                        end if;
                    end if;
                end if;
            end if;
        end if;
    end process;

end Behavioral;

