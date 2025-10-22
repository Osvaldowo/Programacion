library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL; 

entity Trans is
Port ( 
    clk,rst: in STD_LOGIC;
    sw : in STD_LOGIC_VECTOR(7 downto 0);
    LDtx : out STD_LOGIC;
    tx : out STD_LOGIC
);
end Trans;

architecture Arq_Trans of Trans is
    
    signal cnttx_us : UNSIGNED(15 downto 0):= (others => '0');
    signal ttx_us   : UNSIGNED(7 downto 0) := (others => '0');
    
    
    constant BAUDTX_C : STD_LOGIC_VECTOR(15 downto 0) := "0001010001011000"; -- 5208 en binario
    constant BAUDTX_US : UNSIGNED(15 downto 0) := to_unsigned(5207, 16); -- Para la comparación, 5208-1
    
    -- Señales para el 'with select'
    signal ttx : STD_LOGIC_VECTOR(7 downto 0); 
begin
    
    ttx <= STD_LOGIC_VECTOR(ttx_us);

    -- Reloj de transmisión
    process (clk, rst)
    begin
        if (rst='1') then
            cnttx_us <= (others=>'0');
            ttx_us <= (others=>'0');
        elsif (rising_edge(clk)) then
            if (cnttx_us = BAUDTX_US) then -- si alcanzó 5208-1 = 5207
                ttx_us <= ttx_us + 1; -- contador para el transmisor
                cnttx_us <= (others=>'0');
            else
                cnttx_us <= cnttx_us + 1; -- contador del TX
            end if;
        end if;
    end process;
    
    -- Protocolo de transmisión
    with ttx select
    tx <= '1' when X"00",
          '0' when X"01", -- bit de start
          sw(0) when X"02",
          sw(1) when X"03",
          sw(2) when X"04",
          sw(3) when X"05",
          sw(4) when X"06",
          sw(5) when X"07",
          sw(6) when X"08",
          sw(7) when X"09",
          '1' when X"0A", -- bit de stop
          '1' when others;
          
    -- Protocolo de transmisión led testigo
    with ttx select
    LDtx <= '1' when X"00",
            '0' when X"01", -- bit de start
            sw(0) when X"02",
            sw(1) when X"03",
            sw(2) when X"04",
            sw(3) when X"05",
            sw(4) when X"06",
            sw(5) when X"07",
            sw(6) when X"08",
            sw(7) when X"09",
            '1' when X"0A", -- bit de stop
            '0' when others;

end Arq_Trans;