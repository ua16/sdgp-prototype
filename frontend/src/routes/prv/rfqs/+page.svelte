<script>

    import ProviderNav from "$lib/components/provider/ProviderNav.svelte";
    import ProviderContainer from "$lib/components/provider/ProviderContainer.svelte";
    import ProviderRFQs from "$lib/components/provider/ProviderRFQs.svelte";

    import { onMount } from "svelte";

    let isSignedIn = false;
    onMount(() => {
        isSignedIn = localStorage.getItem("signedin") === "true";
    });
</script>

<div>
    {#if isSignedIn === false}
        <p>404 Not Found</p>

    {:else}
        <ProviderContainer>
            <ProviderNav />
            <ProviderRFQs />
        </ProviderContainer>
    {/if}
</div>
