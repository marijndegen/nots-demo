using Microsoft.AspNetCore.Authorization;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace wapp_demo
{
    public class RequireMfa : IAuthorizationRequirement { }
}
