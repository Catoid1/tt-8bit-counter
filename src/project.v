/*
 * Copyright (c) 2026 Adam Dubois
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_counter (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

//8-bit binary counter w/ reset and enable
    wire enable   = ui_in[0];
    wire sync_rst = ui_in[1];

    reg [7:0] count;


    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            count <= 8'b00000000;
        end else if (sync_rst) begin
            count <= 8'b00000000;
        end else if (enable) begin
            count <= count + 1'b1;
        end
    end
  // All output pins must be assigned. If not used, assign to 0.
  assign uo_out  = count;  // Example: ou_out is the sum of ui_in and uio_in
  //assign uio_out = 0;
  //assign uio_oe  = 0;
  assign uio_out = 8'b0;
  assign uio_oe  = 8'b0;   

  // List all unused inputs to prevent warnings
    wire _unused = &{ena, uio_in, ui_in[7:2], 1'b0};

endmodule
