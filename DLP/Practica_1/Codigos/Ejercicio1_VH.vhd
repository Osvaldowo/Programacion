library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Ejercicio1_VH is
    Port (
        -- Entradas
        A : in  STD_LOGIC;
        B : in  STD_LOGIC;
        C : in  STD_LOGIC;
        
        -- Salidas
        S1 : out STD_LOGIC;
        S2 : out STD_LOGIC;
        S3 : out STD_LOGIC;
        S4 : out STD_LOGIC;
        S5 : out STD_LOGIC;
        S6 : out STD_LOGIC
    );
end Ejercicio1_VH;

architecture Behavioral of Ejercicio1_VH is
    -- Señales internas (entradas invertidas)
    signal na, nb, nc : STD_LOGIC;
begin
    -- Invertir entradas
    na <= not A;
    nb <= not B;
    nc <= not C;

    process(na, nb, nc)
    begin
        -- Lógica para S1 (001, 010, 100, 111)
        S1 <= ((not na and not nb and nc) or 
               (not na and nb and not nc) or 
               (na and not nb and not nc) or 
               (na and nb and nc));

        -- Lógica para S2 (todas menos 000)
        S2 <= (na or nb or nc);

        -- Lógica para S3
        S3 <= ((not na and not nb) or (na and nb));

        -- Lógica para S4 (001, 011, 101)
        S4 <= ((not na and nb and nc) or (na and nb and not nc));

        -- Lógica para S5 (000, 011, 100, 111)
        S5 <= (not na and not nb and not nc);

        -- Lógica para S6 (010, 100, 101)
        S6 <= ((na and not nc));
    end process;

end Behavioral;
