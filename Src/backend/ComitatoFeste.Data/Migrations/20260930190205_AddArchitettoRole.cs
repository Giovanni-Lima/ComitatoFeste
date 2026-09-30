using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ComitatoFeste.Data.Migrations
{
    /// <inheritdoc />
    public partial class AddArchitettoRole : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropCheckConstraint(
                name: "CK_Members_Role",
                table: "Members");

            migrationBuilder.AddCheckConstraint(
                name: "CK_Members_Role",
                table: "Members",
                sql: "\"Role\" IN ('lettore', 'amministratore', 'architetto')");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropCheckConstraint(
                name: "CK_Members_Role",
                table: "Members");

            migrationBuilder.AddCheckConstraint(
                name: "CK_Members_Role",
                table: "Members",
                sql: "\"Role\" IN ('lettore', 'amministratore')");
        }
    }
}
