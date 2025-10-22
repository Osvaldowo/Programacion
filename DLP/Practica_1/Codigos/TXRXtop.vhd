library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity TXRXtop is
Port (
    clk,rst: in STD_LOGIC;       
    clk_enc_pin : in  std_logic;         -- Pin CLK (A) del encoder
    dt_enc_pin  : in  std_logic;         -- Pin DT (B) del encoder
    sw_enc_pin  : in  std_logic;         -- Pin SW (Botón) del encoder
    leds: out std_logic_vector(7 downto 0);  -- LD (Muestra el valor RX o TX)
    LDtx : out STD_LOGIC;                -- LED indicador de TX
    tx : out STD_LOGIC;                  -- Salida RS232 TX
    rx : in std_logic
);
end TXRXtop;

architecture Arq_TXRX of TXRXtop is
    
    -- Señal interna para el valor del contador del encoder
    signal encoder_data : std_logic_vector(7 downto 0);

    component Encoder_VHDL
    Port (
        clk     : in  std_logic;
        reset   : in  std_logic;
        clk_pin : in  std_logic;
        dt_pin  : in  std_logic;
        sw_pin  : in  std_logic;
        cout    : out std_logic_vector(7 downto 0)
    );
    end component;

    component Trans
    Port (
        clk: in STD_LOGIC;
        rst: in STD_LOGIC;
        sw : in STD_LOGIC_VECTOR(7 downto 0);
        LDtx : out STD_LOGIC;
        tx : out STD_LOGIC
    );
    end component;

    -- componente U2 RX
    component Recep
    Port (
        clk: in std_logic;
        rst: in std_logic;
        rx: in std_logic;
        leds: out std_logic_vector(7 downto 0)
    );
    end component;

begin
    
    -- INSTANCIA 0: Módulo del Encoder
    U0 : Encoder_VHDL
    port map(
        clk => clk,
        reset => rst,
        clk_pin => clk_enc_pin,
        dt_pin => dt_enc_pin,
        sw_pin => sw_enc_pin,
        cout => encoder_data       -- Salida del encoder
    );

    -- INSTANCIA 1: Módulo Trans
    U1 : Trans
    port map(
        clk => clk,
        rst => rst,
        sw => encoder_data,        -- ¡CONEXIÓN CLAVE! Ahora envía el valor del encoder.
        LDtx => LDtx,
        tx => tx
    );

    -- INSTANCIA 2: Módulo Recep
    U2 : Recep
    port map(
        clk => clk,
        rst => rst,
        rx => rx,
        leds => leds
    );
end Arq_TXRX;