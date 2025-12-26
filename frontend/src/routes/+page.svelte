<script>
    import Navbar from "./Navbar.svelte";
    import Marketing from "./Marketing.svelte";

    import ProviderNav from "$lib/components/provider/ProviderNav.svelte";
    import ProviderContainer from "$lib/components/provider/ProviderContainer.svelte";
    import ProviderDashboard from "$lib/components/provider/ProviderDashboard.svelte";

    import { onMount } from "svelte";

    let isSignedIn = false;
    onMount(() => {
        isSignedIn = localStorage.getItem("signedin") === "true";
    });
</script>

<div>
    {#if isSignedIn === true}
        <Navbar />
        <Marketing />
    {:else}
        <ProviderContainer>
            <ProviderNav />
            <ProviderDashboard />
        </ProviderContainer>
    {/if}
</div>
