using Microsoft.AspNetCore.Authorization;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace wapp_demo
{
    public class RequireMfaHandler : AuthorizationHandler<RequireMfa>
    {
        protected override Task HandleRequirementAsync(
            AuthorizationHandlerContext context,
            RequireMfa requirement)
        {
            if (context == null)
                throw new ArgumentNullException(nameof(context));
            if (requirement == null)
                throw new ArgumentNullException(nameof(requirement));

            var amrClaim =
                context.User.Claims.FirstOrDefault(t => t.Type == "amr");

            Console.WriteLine("someclaim");

            if (amrClaim != null /*&& amrClaim.Value == Amr.Mfa*/ )
            {
                Console.WriteLine("armClaim");
                context.Succeed(requirement);
            }

            context.Fail();

            return Task.CompletedTask;
        }
    }
}
