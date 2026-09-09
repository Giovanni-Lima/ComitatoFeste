using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ComitatoFeste.Data.Migrations
{
    /// <inheritdoc />
    public partial class AddMemberRole : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "Role",
                table: "Members",
                type: "character varying(20)",
                maxLength: 20,
                nullable: false,
                defaultValue: "lettore");

            migrationBuilder.AddCheckConstraint(
                name: "CK_Members_Role",
                table: "Members",
                sql: "\"Role\" IN ('lettore', 'amministratore')");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropCheckConstraint(
                name: "CK_Members_Role",
                table: "Members");

            migrationBuilder.DropColumn(
                name: "Role",
                table: "Members");
        }
    }
}
