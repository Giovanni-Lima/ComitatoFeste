using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ComitatoFeste.Data.Migrations
{
    /// <inheritdoc />
    public partial class AddDigestPointImportant : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<bool>(
                name: "IsImportant",
                table: "DigestPoints",
                type: "boolean",
                nullable: false,
                defaultValue: false);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "IsImportant",
                table: "DigestPoints");
        }
    }
}
