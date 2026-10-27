<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project is an example of a simple 8-bit synchronous binary counter with enable and reset controls I am using to learn the tiny tapeout process:
- **Clock (`clk`)**: Every rising edge of the clock the counter proceeds when enabled.
- **Asynchronous Reset (`rst_n`)**: Active low reset to zero out the counter register asynchronously.
- **Enable (`ui[0]`)**: set high for counting on clock cycles, leave low to stop counter.
- **Synchronous Reset (`ui[1]`)**: Zeros out the register of the counter synchronously, on rising edge of clock when set high.
- **Outputs (`uo[0:7]`)**: Outputs the current binary value of the counter in 8-bits (`uo[0]` is LSB, `uo[7]` is MSB). 

## How to test

1. **Initialize**: Power on and drive asynchronous reset high.
2. **Enable Counting**: Drive 'ui[0]' high.
3. **Verify Output**: Observe the output (`uo[7:0]`) incrementing on clock rising edge.
4. **Test Hold**: Drive 'ui[0]' low and verify that the counter freezes.
5. **Test Sync Reset**: Drive 'ui[1]' to verify reset.
