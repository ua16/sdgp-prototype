<script lang="ts">
    let { quotedata } = $props();
</script>

<div
    class="flex flex-col gap-3 w-full bg-stone-100 border-stone-300 border-2 p-3 text-stone-700 rounded-2xl"
>
    <div class="font-bold text-xl">
        <span>Service Requirements</span>
    </div>

    {#if quotedata.needCargoInsurance === 1}
        <div class="w-full grid place-items-center">
            <div class="flex flex-row rounded-2xl w-9/10 bg-emerald-300 p-3 items-center">
                <div class="w-1/2 text-stone-800 text-lg font-medium">
                    Cargo Insurance
                </div>
                <div class="w-1/2 text-black text-right">Required</div>
            </div>
        </div>
    {:else}
        <div class="w-full grid place-items-center">
            <div class="flex flex-row rounded-2xl w-9/10 bg-rose-300 p-3 items-center">
                <div class="w-1/2 text-stone-800 text-lg font-medium">
                    Cargo Insurance
                </div>
                <div class="w-1/2 text-black text-right">Not Required</div>
            </div>
        </div>
    {/if}

</div>
