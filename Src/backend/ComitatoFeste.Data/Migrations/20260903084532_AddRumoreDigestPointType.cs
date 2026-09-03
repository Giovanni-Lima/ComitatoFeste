using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ComitatoFeste.Data.Migrations
{
    /// <inheritdoc />
    public partial class AddRumoreDigestPointType : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropCheckConstraint(
                name: "CK_DigestPoints_Type",
                table: "DigestPoints");

            migrationBuilder.AddCheckConstraint(
                name: "CK_DigestPoints_Type",
                table: "DigestPoints",
                sql: "\"Type\" IN ('decisione', 'domanda', 'media', 'info', 'rumore')");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropCheckConstraint(
                name: "CK_DigestPoints_Type",
                table: "DigestPoints");

            migrationBuilder.AddCheckConstraint(
                name: "CK_DigestPoints_Type",
                table: "DigestPoints",
                sql: "\"Type\" IN ('decisione', 'domanda', 'media', 'info')");
        }
    }
}
